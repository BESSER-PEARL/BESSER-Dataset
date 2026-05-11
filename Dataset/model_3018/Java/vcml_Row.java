





import java.util.List;
import java.util.ArrayList;

public class vcml_Row  {






    private List<vcml_Literal> vcml_literals;




    private vcml_VariantTableContent vcml_varianttablecontent;


    public vcml_Row(
    ) {
        this.vcml_literals = new ArrayList<>();
    }

    public vcml_Row(
        ArrayList<vcml_Literal> vcml_literals    ) {
        this.vcml_literals = vcml_literals;
    }


    public List<vcml_Literal> getVcml_literals() {
        return vcml_literals;
    }

    public void addVcml_literal(Vcml_literal vcml_literal) {
        this.vcml_literals.add(vcml_literal);
    }
    public vcml_VariantTableContent getVcml_varianttablecontent() {
        return vcml_varianttablecontent;
    }

    public void setVcml_varianttablecontent(vcml_VariantTableContent vcml_varianttablecontent) {
        this.vcml_varianttablecontent = vcml_varianttablecontent;
    }

}