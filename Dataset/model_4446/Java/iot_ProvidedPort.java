




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class iot_ProvidedPort  {

    private String name;
    private String UUID;



    public iot_ProvidedPort(
        String name,        String UUID    ) {
        this.name = name;
        this.UUID = UUID;
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


}