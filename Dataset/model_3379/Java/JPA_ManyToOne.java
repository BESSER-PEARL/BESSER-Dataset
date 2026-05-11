





import java.util.List;
import java.util.ArrayList;

public class JPA_ManyToOne extends Anotation {

    private String fetch;
    private boolean nullable;
    private String joinColumn;



    public JPA_ManyToOne(
        String fetch,        boolean nullable,        String joinColumn    ) {
        super(
        );
        this.fetch = fetch;
        this.nullable = nullable;
        this.joinColumn = joinColumn;
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
    public String getJoincolumn() {
        return joinColumn;
    }

    public void setJoincolumn(String joinColumn) {
        this.joinColumn = joinColumn;
    }


}