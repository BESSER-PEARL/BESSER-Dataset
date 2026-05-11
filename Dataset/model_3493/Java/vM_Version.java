





import java.util.List;
import java.util.ArrayList;

public class vM_Version  {

    private int main;
    private int tail;





    private vM_MetaDataDeclaration vm_metadatadeclaration;


    public vM_Version(
        int main,        int tail    ) {
        this.main = main;
        this.tail = tail;
    }


    public int getMain() {
        return main;
    }

    public void setMain(int main) {
        this.main = main;
    }
    public int getTail() {
        return tail;
    }

    public void setTail(int tail) {
        this.tail = tail;
    }

    public vM_MetaDataDeclaration getVm_metadatadeclaration() {
        return vm_metadatadeclaration;
    }

    public void setVm_metadatadeclaration(vM_MetaDataDeclaration vm_metadatadeclaration) {
        this.vm_metadatadeclaration = vm_metadatadeclaration;
    }

}