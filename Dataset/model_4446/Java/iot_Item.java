




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class iot_Item  {

    private String name;
    private String UUID;
    private boolean newThread;





    private iot_Software iot_software;




    private iot_ProvidedPort iot_providedport;


    public iot_Item(
        String name,        String UUID,        boolean newThread    ) {
        this.name = name;
        this.UUID = UUID;
        this.newThread = newThread;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUuid() {
        return UUID;
    }

    public void setUuid(String UUID) {
        this.UUID = UUID;
    }
    public boolean getNewthread() {
        return newThread;
    }

    public void setNewthread(boolean newThread) {
        this.newThread = newThread;
    }

    public iot_Software getIot_software() {
        return iot_software;
    }

    public void setIot_software(iot_Software iot_software) {
        this.iot_software = iot_software;
    }
    public iot_ProvidedPort getIot_providedport() {
        return iot_providedport;
    }

    public void setIot_providedport(iot_ProvidedPort iot_providedport) {
        this.iot_providedport = iot_providedport;
    }

}