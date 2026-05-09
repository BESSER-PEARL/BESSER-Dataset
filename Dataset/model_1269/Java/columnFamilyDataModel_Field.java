





import java.util.List;
import java.util.ArrayList;

public class columnFamilyDataModel_Field  {

    private String name;





    private columnFamilyDataModel_Type columnfamilydatamodel_type;




    private columnFamilyDataModel_UserDefinedType columnfamilydatamodel_userdefinedtype;


    public columnFamilyDataModel_Field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public columnFamilyDataModel_Type getColumnfamilydatamodel_type() {
        return columnfamilydatamodel_type;
    }

    public void setColumnfamilydatamodel_type(columnFamilyDataModel_Type columnfamilydatamodel_type) {
        this.columnfamilydatamodel_type = columnfamilydatamodel_type;
    }
    public columnFamilyDataModel_UserDefinedType getColumnfamilydatamodel_userdefinedtype() {
        return columnfamilydatamodel_userdefinedtype;
    }

    public void setColumnfamilydatamodel_userdefinedtype(columnFamilyDataModel_UserDefinedType columnfamilydatamodel_userdefinedtype) {
        this.columnfamilydatamodel_userdefinedtype = columnfamilydatamodel_userdefinedtype;
    }

}