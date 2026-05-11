





import java.util.List;
import java.util.ArrayList;

public class JPA_Column extends Anotation {

    private String name;
    private boolean nullable;
    private String type;
    private String fetch;



    public JPA_Column(
        String name,        boolean nullable,        String type,        String fetch    ) {
        super(
        );
        this.name = name;
        this.nullable = nullable;
        this.type = type;
        this.fetch = fetch;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }


}