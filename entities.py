class ResourceConstraints:
    def __init__(self, maximum):
        """
        :type  maximum: float
        """
        self.maximum = maximum

    def __str__(self):
        return str(self.maximum)

    def __repr__(self):
        return self.__str__()


class Task:
    def __init__(self, cpu_constr, ram_constr, time_constr):
        """
        :type cpu_constr: ResourceConstraints
        :type ram_constr: ResourceConstraints
        :type time_constr: ResourceConstraints
        """
        self.cpu_constr = cpu_constr
        self.ram_constr = ram_constr
        self.time_constr = time_constr

    def __str__(self):
        return 'CPU: %s  RAM: %s  TIME: %s' % (self.cpu_constr, self.ram_constr, self.time_constr)

    def __repr__(self):
        return self.__str__()


class Machine:
    def __init__(self, ram_capacity, ram_usage, millicores, millicores_usage):
        """
        :type ram_capacity: float
        :type ram_usage: float
        :type millicores: float
        :type millicores_usage: float
        """
        self.ram_capacity = ram_capacity
        self.ram_usage = ram_usage
        self.millicores = millicores
        self.millicores_usage = millicores_usage

    def __str__(self):
        return 'RAM_CAPACITY: %s  RAM_USAGE: %s  MILLICORES: %s MILLICORES_USAGE %s'\
               % (self.ram_capacity, self.ram_usage, self.millicores,  self.millicores_usage)

    def __repr__(self):
        return self.__str__()
