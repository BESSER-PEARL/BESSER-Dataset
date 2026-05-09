





import java.util.List;
import java.util.ArrayList;

public class express_core_Scope  {






    private List<Remark> remarks;




    private List<NamedElement> namedelements;


    public express_core_Scope(
    ) {
        this.remarks = new ArrayList<>();
        this.namedelements = new ArrayList<>();
    }

    public express_core_Scope(
        ArrayList<Remark> remarks,        ArrayList<NamedElement> namedelements    ) {
        this.remarks = remarks;
        this.namedelements = namedelements;
    }


    public List<Remark> getRemarks() {
        return remarks;
    }

    public void addRemark(Remark remark) {
        this.remarks.add(remark);
    }
    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}