





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_SimpleNameCS extends TypeLiteralExpCS, VariableExpCS, TypeCS, CollectionLiteralExpCS {

    private String value;





    private List<essentialOCLCST_CollectionLiteralPartCS> essentialoclcst_collectionliteralpartcss;




    private essentialOCLCST_VariableCS essentialoclcst_variablecs;




    private essentialOCLCST_CollectionTypeCS essentialoclcst_collectiontypecs;


    public essentialOCLCST_SimpleNameCS(
        String value    ) {
        super(
        );
        this.value = value;
        this.essentialoclcst_collectionliteralpartcss = new ArrayList<>();
    }

    public essentialOCLCST_SimpleNameCS(
        String value        ArrayList<essentialOCLCST_CollectionLiteralPartCS> essentialoclcst_collectionliteralpartcss    ) {
        this.value = value;
        this.essentialoclcst_collectionliteralpartcss = essentialoclcst_collectionliteralpartcss;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<essentialOCLCST_CollectionLiteralPartCS> getEssentialoclcst_collectionliteralpartcss() {
        return essentialoclcst_collectionliteralpartcss;
    }

    public void addEssentialoclcst_collectionliteralpartcs(Essentialoclcst_collectionliteralpartcs essentialoclcst_collectionliteralpartcs) {
        this.essentialoclcst_collectionliteralpartcss.add(essentialoclcst_collectionliteralpartcs);
    }
    public essentialOCLCST_VariableCS getEssentialoclcst_variablecs() {
        return essentialoclcst_variablecs;
    }

    public void setEssentialoclcst_variablecs(essentialOCLCST_VariableCS essentialoclcst_variablecs) {
        this.essentialoclcst_variablecs = essentialoclcst_variablecs;
    }
    public essentialOCLCST_CollectionTypeCS getEssentialoclcst_collectiontypecs() {
        return essentialoclcst_collectiontypecs;
    }

    public void setEssentialoclcst_collectiontypecs(essentialOCLCST_CollectionTypeCS essentialoclcst_collectiontypecs) {
        this.essentialoclcst_collectiontypecs = essentialoclcst_collectiontypecs;
    }

}