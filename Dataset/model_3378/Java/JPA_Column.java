





import java.util.List;
import java.util.ArrayList;

public class JPA_Column extends Anotation {

    private String fetch;
    private String type;
    private String name;
    private boolean nullable;



    public JPA_Column(
        String fetch,        String type,        String name,        boolean nullable    ) {
        super(
        );
        this.fetch = fetch;
        this.type = type;
        this.name = name;
        this.nullable = nullable;
    }


    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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


}