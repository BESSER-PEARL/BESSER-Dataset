





import java.util.List;
import java.util.ArrayList;

public class eTJ_Column  {

    private String id;





    private eTJ_Columns etj_columns;




    private eTJ_ExtendedResourceAttributeColumn etj_extendedresourceattributecolumn;




    private List<eTJ_ColumnAttribute> etj_columnattributes;


    public eTJ_Column(
        String id    ) {
        this.id = id;
        this.etj_columnattributes = new ArrayList<>();
    }

    public eTJ_Column(
        String id        ArrayList<eTJ_ColumnAttribute> etj_columnattributes    ) {
        this.id = id;
        this.etj_columnattributes = etj_columnattributes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public eTJ_Columns getEtj_columns() {
        return etj_columns;
    }

    public void setEtj_columns(eTJ_Columns etj_columns) {
        this.etj_columns = etj_columns;
    }
    public eTJ_ExtendedResourceAttributeColumn getEtj_extendedresourceattributecolumn() {
        return etj_extendedresourceattributecolumn;
    }

    public void setEtj_extendedresourceattributecolumn(eTJ_ExtendedResourceAttributeColumn etj_extendedresourceattributecolumn) {
        this.etj_extendedresourceattributecolumn = etj_extendedresourceattributecolumn;
    }
    public List<eTJ_ColumnAttribute> getEtj_columnattributes() {
        return etj_columnattributes;
    }

    public void addEtj_columnattribute(Etj_columnattribute etj_columnattribute) {
        this.etj_columnattributes.add(etj_columnattribute);
    }

}