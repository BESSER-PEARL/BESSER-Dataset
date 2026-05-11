





import java.util.List;
import java.util.ArrayList;

public class JPA_Column extends Anotation {

    private String type;
    private String fetch;
    private boolean nullable;
    private String name;



    public JPA_Column(
        String type,        String fetch,        boolean nullable,        String name    ) {
        super(
        );
        this.type = type;
        this.fetch = fetch;
        this.nullable = nullable;
        this.name = name;
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
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}