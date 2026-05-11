





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_VirtualMachineFeature  {

    private String name;
    private String many;





    private giraffeDSL_Create giraffedsl_create;




    private giraffeDSL_VirtualMachine giraffedsl_virtualmachine;


    public giraffeDSL_VirtualMachineFeature(
        String name,        String many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public giraffeDSL_VirtualMachine getGiraffedsl_virtualmachine() {
        return giraffedsl_virtualmachine;
    }

    public void setGiraffedsl_virtualmachine(giraffeDSL_VirtualMachine giraffedsl_virtualmachine) {
        this.giraffedsl_virtualmachine = giraffedsl_virtualmachine;
    }

}