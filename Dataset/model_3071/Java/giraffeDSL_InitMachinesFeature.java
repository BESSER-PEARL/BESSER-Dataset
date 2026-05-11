





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_InitMachinesFeature  {

    private String name;
    private int type;
    private String many;





    private giraffeDSL_Create giraffedsl_create;


    public giraffeDSL_InitMachinesFeature(
        String name,        int type,        String many    ) {
        this.name = name;
        this.type = type;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }

    public giraffeDSL_Create getGiraffedsl_create() {
        return giraffedsl_create;
    }

    public void setGiraffedsl_create(giraffeDSL_Create giraffedsl_create) {
        this.giraffedsl_create = giraffedsl_create;
    }

}