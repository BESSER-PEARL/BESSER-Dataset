





import java.util.List;
import java.util.ArrayList;

public class pascal_bound_specification  {

    private String id3;
    private String id2;
    private String id1;





    private pascal_unpacked_conformant_array_Schema pascal_unpacked_conformant_array_schema;




    private pascal_packed_conformant_array_schema pascal_packed_conformant_array_schema;


    public pascal_bound_specification(
        String id3,        String id2,        String id1    ) {
        this.id3 = id3;
        this.id2 = id2;
        this.id1 = id1;
    }


    public String getId3() {
        return id3;
    }

    public void setId3(String id3) {
        this.id3 = id3;
    }
    public String getId2() {
        return id2;
    }

    public void setId2(String id2) {
        this.id2 = id2;
    }
    public String getId1() {
        return id1;
    }

    public void setId1(String id1) {
        this.id1 = id1;
    }

    public pascal_unpacked_conformant_array_Schema getPascal_unpacked_conformant_array_schema() {
        return pascal_unpacked_conformant_array_schema;
    }

    public void setPascal_unpacked_conformant_array_schema(pascal_unpacked_conformant_array_Schema pascal_unpacked_conformant_array_schema) {
        this.pascal_unpacked_conformant_array_schema = pascal_unpacked_conformant_array_schema;
    }
    public pascal_packed_conformant_array_schema getPascal_packed_conformant_array_schema() {
        return pascal_packed_conformant_array_schema;
    }

    public void setPascal_packed_conformant_array_schema(pascal_packed_conformant_array_schema pascal_packed_conformant_array_schema) {
        this.pascal_packed_conformant_array_schema = pascal_packed_conformant_array_schema;
    }

}