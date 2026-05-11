





import java.util.List;
import java.util.ArrayList;

public class pascal_bound_specification  {

    private String name;
    private String final;
    private String initial;





    private pascal_packed_conformant_array_schema pascal_packed_conformant_array_schema;




    private pascal_unpacked_conformant_array_schema pascal_unpacked_conformant_array_schema;


    public pascal_bound_specification(
        String name,        String final,        String initial    ) {
        this.name = name;
        this.final = final;
        this.initial = initial;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getInitial() {
        return initial;
    }

    public void setInitial(String initial) {
        this.initial = initial;
    }

    public pascal_packed_conformant_array_schema getPascal_packed_conformant_array_schema() {
        return pascal_packed_conformant_array_schema;
    }

    public void setPascal_packed_conformant_array_schema(pascal_packed_conformant_array_schema pascal_packed_conformant_array_schema) {
        this.pascal_packed_conformant_array_schema = pascal_packed_conformant_array_schema;
    }
    public pascal_unpacked_conformant_array_schema getPascal_unpacked_conformant_array_schema() {
        return pascal_unpacked_conformant_array_schema;
    }

    public void setPascal_unpacked_conformant_array_schema(pascal_unpacked_conformant_array_schema pascal_unpacked_conformant_array_schema) {
        this.pascal_unpacked_conformant_array_schema = pascal_unpacked_conformant_array_schema;
    }

}