





import java.util.List;
import java.util.ArrayList;

public class opf_Guide  {






    private opf_Package opf_package;




    private List<opf_Reference> opf_references;


    public opf_Guide(
    ) {
        this.opf_references = new ArrayList<>();
    }

    public opf_Guide(
        ArrayList<opf_Reference> opf_references    ) {
        this.opf_references = opf_references;
    }


    public opf_Package getOpf_package() {
        return opf_package;
    }

    public void setOpf_package(opf_Package opf_package) {
        this.opf_package = opf_package;
    }
    public List<opf_Reference> getOpf_references() {
        return opf_references;
    }

    public void addOpf_reference(Opf_reference opf_reference) {
        this.opf_references.add(opf_reference);
    }

}