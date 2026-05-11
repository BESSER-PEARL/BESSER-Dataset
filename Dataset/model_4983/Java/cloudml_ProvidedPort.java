





import java.util.List;
import java.util.ArrayList;

public class cloudml_ProvidedPort extends Port {






    private cloudml_Relationship cloudml_relationship;




    private cloudml_Component cloudml_component;


    public cloudml_ProvidedPort(
    ) {
        super(
        );
    }



    public cloudml_Relationship getCloudml_relationship() {
        return cloudml_relationship;
    }

    public void setCloudml_relationship(cloudml_Relationship cloudml_relationship) {
        this.cloudml_relationship = cloudml_relationship;
    }
    public cloudml_Component getCloudml_component() {
        return cloudml_component;
    }

    public void setCloudml_component(cloudml_Component cloudml_component) {
        this.cloudml_component = cloudml_component;
    }

}