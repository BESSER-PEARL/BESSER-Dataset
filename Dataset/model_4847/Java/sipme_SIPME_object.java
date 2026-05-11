




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class sipme_SIPME_object  {

    private String name;
    private String UUID;
    private String description;



    public sipme_SIPME_object(
        String name,        String UUID,        String description    ) {
        this.name = name;
        this.UUID = UUID;
        this.description = description;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}