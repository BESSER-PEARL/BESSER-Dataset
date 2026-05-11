





import java.util.List;
import java.util.ArrayList;

public class vcml_BOMItem  {

    private int itemnumber;





    private vcml_BillOfMaterial vcml_billofmaterial;




    private vcml_SelectionCondition vcml_selectioncondition;


    public vcml_BOMItem(
        int itemnumber    ) {
        this.itemnumber = itemnumber;
    }


    public int getItemnumber() {
        return itemnumber;
    }

    public void setItemnumber(int itemnumber) {
        this.itemnumber = itemnumber;
    }

    public vcml_BillOfMaterial getVcml_billofmaterial() {
        return vcml_billofmaterial;
    }

    public void setVcml_billofmaterial(vcml_BillOfMaterial vcml_billofmaterial) {
        this.vcml_billofmaterial = vcml_billofmaterial;
    }
    public vcml_SelectionCondition getVcml_selectioncondition() {
        return vcml_selectioncondition;
    }

    public void setVcml_selectioncondition(vcml_SelectionCondition vcml_selectioncondition) {
        this.vcml_selectioncondition = vcml_selectioncondition;
    }

}