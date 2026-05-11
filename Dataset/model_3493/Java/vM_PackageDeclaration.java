





import java.util.List;
import java.util.ArrayList;

public class vM_PackageDeclaration extends VmBlock {

    private String name;





    private List<vM_VmBlock> vm_vmblocks;


    public vM_PackageDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.vm_vmblocks = new ArrayList<>();
    }

    public vM_PackageDeclaration(
        String name        ArrayList<vM_VmBlock> vm_vmblocks    ) {
        this.name = name;
        this.vm_vmblocks = vm_vmblocks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<vM_VmBlock> getVm_vmblocks() {
        return vm_vmblocks;
    }

    public void addVm_vmblock(Vm_vmblock vm_vmblock) {
        this.vm_vmblocks.add(vm_vmblock);
    }

}