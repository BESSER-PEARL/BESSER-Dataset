





import java.util.List;
import java.util.ArrayList;

public class myDsl_RestModel extends Type {

    private String self;
    private String id;





    private myDsl_RestModel mydsl_restmodel;


    public myDsl_RestModel(
        String self,        String id    ) {
        super(
        );
        this.self = self;
        this.id = id;
    }


    public String getSelf() {
        return self;
    }

    public void setSelf(String self) {
        this.self = self;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_RestModel getMydsl_restmodel() {
        return mydsl_restmodel;
    }

    public void setMydsl_restmodel(myDsl_RestModel mydsl_restmodel) {
        this.mydsl_restmodel = mydsl_restmodel;
    }

}