# LogReader
# - fd:
# - partitial_result: A string that records half-read last line.
class LogReader(object):
    """log reader reads and returns the newly written entries"""

    def __init__(self, path):
        fd = open(path)
        # seek file to the end.
        # then traverse back to the last '\n' or beginning.
        fd.seek(0, 2)

        while fd.tell() > 0:
            fd.seek(-1, 1)
            if fd.read(1) == '\n':
                break
            # offset the read(1)
            fd.seek(-1, 1)

        self.fd = fd
        self.partitial_result = ''

    def readlines(self):
        result = self.fd.readlines()

        if len(result) == 0:
            return []

        # Complete the whole line for the last cut-in.
        if len(self.partitial_result) > 0:
            result[0] = self.partitial_result + result[0]
            if result[0][-1] == '\n':
                self.partitial_result = ''

        if result[-1][-1] == '\n':
            return result

        # Save the last incomplete cut-in line for next read.
        self.partitial_result += result[-1]
        return result[:-1]

    def close(self):
        self.fd.close()
