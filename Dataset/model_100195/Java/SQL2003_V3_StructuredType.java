





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_StructuredType extends UserDefinedType {

    private boolean is_final;
    private boolean is_instantiable;





    private SQL2003_V3_Attribute sql2003_v3_attribute;




    private List<SQL2003_V3_Attribute> sql2003_v3_attributes;




    private SQL2003_V3_StructuredType sql2003_v3_structuredtype;


    public SQL2003_V3_StructuredType(
        boolean is_final,        boolean is_instantiable    ) {
        super(
        );
        this.is_final = is_final;
        this.is_instantiable = is_instantiable;
        this.sql2003_v3_attributes = new ArrayList<>();
    }

    public SQL2003_V3_StructuredType(
        boolean is_final,        boolean is_instantiable        ArrayList<SQL2003_V3_Attribute> sql2003_v3_attributes    ) {
        this.is_final = is_final;
        this.is_instantiable = is_instantiable;
        this.sql2003_v3_attributes = sql2003_v3_attributes;
    }

    public boolean getIs_final() {
        return is_final;
    }

    public void setIs_final(boolean is_final) {
        this.is_final = is_final;
    }
    public boolean getIs_instantiable() {
        return is_instantiable;
    }

    public void setIs_instantiable(boolean is_instantiable) {
        this.is_instantiable = is_instantiable;
    }

    public SQL2003_V3_Attribute getSql2003_v3_attribute() {
        return sql2003_v3_attribute;
    }

    public void setSql2003_v3_attribute(SQL2003_V3_Attribute sql2003_v3_attribute) {
        this.sql2003_v3_attribute = sql2003_v3_attribute;
    }
    public List<SQL2003_V3_Attribute> getSql2003_v3_attributes() {
        return sql2003_v3_attributes;
    }

    public void addSql2003_v3_attribute(Sql2003_v3_attribute sql2003_v3_attribute) {
        this.sql2003_v3_attributes.add(sql2003_v3_attribute);
    }
    public SQL2003_V3_StructuredType getSql2003_v3_structuredtype() {
        return sql2003_v3_structuredtype;
    }

    public void setSql2003_v3_structuredtype(SQL2003_V3_StructuredType sql2003_v3_structuredtype) {
        this.sql2003_v3_structuredtype = sql2003_v3_structuredtype;
    }

}