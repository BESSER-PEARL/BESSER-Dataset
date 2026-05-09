





import java.util.List;
import java.util.ArrayList;

public class dsl_EnumConstant  {

    private String id;





    private dsl_EnumBody dsl_enumbody;




    private dsl_ClassOrInterfaceBody dsl_classorinterfacebody;


    public dsl_EnumConstant(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_EnumBody getDsl_enumbody() {
        return dsl_enumbody;
    }

    public void setDsl_enumbody(dsl_EnumBody dsl_enumbody) {
        this.dsl_enumbody = dsl_enumbody;
    }
    public dsl_ClassOrInterfaceBody getDsl_classorinterfacebody() {
        return dsl_classorinterfacebody;
    }

    public void setDsl_classorinterfacebody(dsl_ClassOrInterfaceBody dsl_classorinterfacebody) {
        this.dsl_classorinterfacebody = dsl_classorinterfacebody;
    }

}