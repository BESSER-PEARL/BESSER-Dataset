





import java.util.List;
import java.util.ArrayList;

public class HAL_ArticleRetro extends Article {

    private String dateRedaction;





    private AbstractDepot abstractdepot;


    public HAL_ArticleRetro(
        String dateRedaction    ) {
        super(
        );
        this.dateRedaction = dateRedaction;
    }


    public String getDateredaction() {
        return dateRedaction;
    }

    public void setDateredaction(String dateRedaction) {
        this.dateRedaction = dateRedaction;
    }

    public AbstractDepot getAbstractdepot() {
        return abstractdepot;
    }

    public void setAbstractdepot(AbstractDepot abstractdepot) {
        this.abstractdepot = abstractdepot;
    }

}