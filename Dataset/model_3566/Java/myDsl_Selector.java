





import java.util.List;
import java.util.ArrayList;

public class myDsl_Selector  {

    private String id;





    private myDsl_PrimaryExprLinha mydsl_primaryexprlinha;


    public myDsl_Selector(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_PrimaryExprLinha getMydsl_primaryexprlinha() {
        return mydsl_primaryexprlinha;
    }

    public void setMydsl_primaryexprlinha(myDsl_PrimaryExprLinha mydsl_primaryexprlinha) {
        this.mydsl_primaryexprlinha = mydsl_primaryexprlinha;
    }

}