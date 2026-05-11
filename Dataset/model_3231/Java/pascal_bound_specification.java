





import java.util.List;
import java.util.ArrayList;

public class pascal_bound_specification  {

    private String name;
    private String init;
    private String fin;





    private pascal_packed_conformant_array_schema pascal_packed_conformant_array_schema;




    private pascal_unpacked_conformant_array_schema pascal_unpacked_conformant_array_schema;


    public pascal_bound_specification(
        String name,        String init,        String fin    ) {
        this.name = name;
        this.init = init;
        this.fin = fin;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInit() {
        return init;
    }

    public void setInit(String init) {
        this.init = init;
    }
    public String getFin() {
        return fin;
    }

    public void setFin(String fin) {
        this.fin = fin;
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