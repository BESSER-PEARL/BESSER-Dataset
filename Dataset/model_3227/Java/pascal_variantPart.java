





import java.util.List;
import java.util.ArrayList;

public class pascal_variantPart  {






    private pascal_tag pascal_tag;




    private pascal_variant pascal_variant;




    private pascal_fieldList pascal_fieldlist;




    private List<pascal_variant> pascal_variants;




    private pascal_fieldList pascal_fieldlist;


    public pascal_variantPart(
    ) {
        this.pascal_variants = new ArrayList<>();
    }

    public pascal_variantPart(
        ArrayList<pascal_variant> pascal_variants    ) {
        this.pascal_variants = pascal_variants;
    }


    public pascal_tag getPascal_tag() {
        return pascal_tag;
    }

    public void setPascal_tag(pascal_tag pascal_tag) {
        this.pascal_tag = pascal_tag;
    }
    public pascal_variant getPascal_variant() {
        return pascal_variant;
    }

    public void setPascal_variant(pascal_variant pascal_variant) {
        this.pascal_variant = pascal_variant;
    }
    public pascal_fieldList getPascal_fieldlist() {
        return pascal_fieldlist;
    }

    public void setPascal_fieldlist(pascal_fieldList pascal_fieldlist) {
        this.pascal_fieldlist = pascal_fieldlist;
    }
    public List<pascal_variant> getPascal_variants() {
        return pascal_variants;
    }

    public void addPascal_variant(Pascal_variant pascal_variant) {
        this.pascal_variants.add(pascal_variant);
    }
    public pascal_fieldList getPascal_fieldlist() {
        return pascal_fieldlist;
    }

    public void setPascal_fieldlist(pascal_fieldList pascal_fieldlist) {
        this.pascal_fieldlist = pascal_fieldlist;
    }

}