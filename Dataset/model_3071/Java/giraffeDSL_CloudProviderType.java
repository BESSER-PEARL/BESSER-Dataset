





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_CloudProviderType  {

    private String many;
    private String name;





    private giraffeDSL_VirtualMachine giraffedsl_virtualmachine;




    private giraffeDSL_CloudProvider giraffedsl_cloudprovider;


    public giraffeDSL_CloudProviderType(
        String many,        String name    ) {
        this.many = many;
        this.name = name;
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

    public giraffeDSL_VirtualMachine getGiraffedsl_virtualmachine() {
        return giraffedsl_virtualmachine;
    }

    public void setGiraffedsl_virtualmachine(giraffeDSL_VirtualMachine giraffedsl_virtualmachine) {
        this.giraffedsl_virtualmachine = giraffedsl_virtualmachine;
    }
    public giraffeDSL_CloudProvider getGiraffedsl_cloudprovider() {
        return giraffedsl_cloudprovider;
    }

    public void setGiraffedsl_cloudprovider(giraffeDSL_CloudProvider giraffedsl_cloudprovider) {
        this.giraffedsl_cloudprovider = giraffedsl_cloudprovider;
    }

}