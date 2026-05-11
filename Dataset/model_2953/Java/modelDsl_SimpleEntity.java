





import java.util.List;
import java.util.ArrayList;

public class modelDsl_SimpleEntity extends Entity {

    private String implementation;





    private modelDsl_SimpleEntity modeldsl_simpleentity;


    public modelDsl_SimpleEntity(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public modelDsl_SimpleEntity getModeldsl_simpleentity() {
        return modeldsl_simpleentity;
    }

    public void setModeldsl_simpleentity(modelDsl_SimpleEntity modeldsl_simpleentity) {
        this.modeldsl_simpleentity = modeldsl_simpleentity;
    }

}