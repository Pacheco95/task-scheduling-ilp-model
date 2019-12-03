class ResourceConstraints:
    def __init__(self, desired: float):
        """
        :type  desired: float
        """
        self.desired = float(desired)

    def __str__(self):
        return str('%-10s' % self.desired)

    def __repr__(self):
        return self.__str__()


class Task:
    def __init__(self, cpu_constr, ram_constr, time_constr, requires_video_card=False):
        """
        :type cpu_constr: ResourceConstraints
        :type ram_constr: ResourceConstraints
        :type time_constr: ResourceConstraints
        :type requires_video_card: bool
        """
        self.cpu_constr = cpu_constr
        self.ram_constr = ram_constr
        self.time_constr = time_constr
        self.requires_video_card = requires_video_card

    def __str__(self):
        return 'CPU: %s RAM: %s TIME: %s' % (self.cpu_constr, self.ram_constr, self.time_constr)

    def __repr__(self):
        return self.__str__()


class Machine:
    def __init__(self, ram_capacity, ram_usage, millicores, millicores_usage, has_video_card=False):
        """
        :type ram_capacity: float
        :type ram_usage: float
        :type millicores: float
        :type millicores_usage: float
        :type has_video_card: bool
        """
        self.ram_capacity = ram_capacity
        self.ram_usage = ram_usage
        self.millicores = millicores
        self.millicores_usage = millicores_usage
        self.has_video_card = has_video_card

    def __str__(self):
        return 'RAM_CAP: %-10s RAM_USAGE: %-6s MILLICORES: %-10s MILLICORES_USAGE %s'\
               % (self.ram_capacity, self.ram_usage, self.millicores,  self.millicores_usage)

    def __repr__(self):
        return self.__str__()
