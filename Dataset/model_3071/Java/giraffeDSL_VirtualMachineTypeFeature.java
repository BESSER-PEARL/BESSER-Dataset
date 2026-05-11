





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_VirtualMachineTypeFeature  {

    private String many;
    private String name;
    private String type;





    private giraffeDSL_VirtualMachine giraffedsl_virtualmachine;


    public giraffeDSL_VirtualMachineTypeFeature(
        String many,        String name,        String type    ) {
        this.many = many;
        this.name = name;
        this.type = type;
    }


    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public giraffeDSL_VirtualMachine getGiraffedsl_virtualmachine() {
        return giraffedsl_virtualmachine;
    }

    public void setGiraffedsl_virtualmachine(giraffeDSL_VirtualMachine giraffedsl_virtualmachine) {
        this.giraffedsl_virtualmachine = giraffedsl_virtualmachine;
    }

}