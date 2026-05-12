





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_StructuredType extends UserDefinedType {

    private boolean is_instantiable;
    private boolean is_final;





    private SQL2003_evo_Attribute sql2003_evo_attribute;




    private List<SQL2003_evo_Attribute> sql2003_evo_attributes;




    private SQL2003_evo_StructuredType sql2003_evo_structuredtype;


    public SQL2003_evo_StructuredType(
        boolean is_instantiable,        boolean is_final    ) {
        super(
        );
        this.is_instantiable = is_instantiable;
        this.is_final = is_final;
        this.sql2003_evo_attributes = new ArrayList<>();
    }

    public SQL2003_evo_StructuredType(
        boolean is_instantiable,        boolean is_final        ArrayList<SQL2003_evo_Attribute> sql2003_evo_attributes    ) {
        this.is_instantiable = is_instantiable;
        this.is_final = is_final;
        this.sql2003_evo_attributes = sql2003_evo_attributes;
    }

    public boolean getIs_instantiable() {
        return is_instantiable;
    }

    public void setIs_instantiable(boolean is_instantiable) {
        this.is_instantiable = is_instantiable;
    }
    public boolean getIs_final() {
        return is_final;
    }

    public void setIs_final(boolean is_final) {
        this.is_final = is_final;
    }

    public SQL2003_evo_Attribute getSql2003_evo_attribute() {
        return sql2003_evo_attribute;
    }

    public void setSql2003_evo_attribute(SQL2003_evo_Attribute sql2003_evo_attribute) {
        this.sql2003_evo_attribute = sql2003_evo_attribute;
    }
    public List<SQL2003_evo_Attribute> getSql2003_evo_attributes() {
        return sql2003_evo_attributes;
    }

    public void addSql2003_evo_attribute(Sql2003_evo_attribute sql2003_evo_attribute) {
        this.sql2003_evo_attributes.add(sql2003_evo_attribute);
    }
    public SQL2003_evo_StructuredType getSql2003_evo_structuredtype() {
        return sql2003_evo_structuredtype;
    }

    public void setSql2003_evo_structuredtype(SQL2003_evo_StructuredType sql2003_evo_structuredtype) {
        this.sql2003_evo_structuredtype = sql2003_evo_structuredtype;
    }

}