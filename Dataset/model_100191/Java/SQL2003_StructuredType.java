





import java.util.List;
import java.util.ArrayList;

public class SQL2003_StructuredType extends UserDefinedType {

    private boolean is_instantiable;
    private boolean is_final;





    private SQL2003_StructuredType sql2003_structuredtype;




    private SQL2003_Attribute sql2003_attribute;




    private List<SQL2003_Attribute> sql2003_attributes;


    public SQL2003_StructuredType(
        boolean is_instantiable,        boolean is_final    ) {
        super(
        );
        this.is_instantiable = is_instantiable;
        this.is_final = is_final;
        this.sql2003_attributes = new ArrayList<>();
    }

    public SQL2003_StructuredType(
        boolean is_instantiable,        boolean is_final        ArrayList<SQL2003_Attribute> sql2003_attributes    ) {
        this.is_instantiable = is_instantiable;
        this.is_final = is_final;
        this.sql2003_attributes = sql2003_attributes;
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

    public SQL2003_StructuredType getSql2003_structuredtype() {
        return sql2003_structuredtype;
    }

    public void setSql2003_structuredtype(SQL2003_StructuredType sql2003_structuredtype) {
        this.sql2003_structuredtype = sql2003_structuredtype;
    }
    public SQL2003_Attribute getSql2003_attribute() {
        return sql2003_attribute;
    }

    public void setSql2003_attribute(SQL2003_Attribute sql2003_attribute) {
        this.sql2003_attribute = sql2003_attribute;
    }
    public List<SQL2003_Attribute> getSql2003_attributes() {
        return sql2003_attributes;
    }

    public void addSql2003_attribute(Sql2003_attribute sql2003_attribute) {
        this.sql2003_attributes.add(sql2003_attribute);
    }

}