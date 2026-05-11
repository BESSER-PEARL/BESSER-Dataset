




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class iot_RequiredPort  {

    private String UUID;
    private String args;
    private String name;
    private String method;





    private iot_ProvidedPort iot_providedport;




    private iot_Iteration iot_iteration;


    public iot_RequiredPort(
        String UUID,        String args,        String name,        String method    ) {
        this.UUID = UUID;
        this.args = args;
        this.name = name;
        this.method = method;
    }


    public String getUuid() {
        return UUID;
    }

    public void setUuid(String UUID) {
        this.UUID = UUID;
    }
    public String getArgs() {
        return args;
    }

    public void setArgs(String args) {
        this.args = args;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public iot_ProvidedPort getIot_providedport() {
        return iot_providedport;
    }

    public void setIot_providedport(iot_ProvidedPort iot_providedport) {
        this.iot_providedport = iot_providedport;
    }
    public iot_Iteration getIot_iteration() {
        return iot_iteration;
    }

    public void setIot_iteration(iot_Iteration iot_iteration) {
        this.iot_iteration = iot_iteration;
    }

}