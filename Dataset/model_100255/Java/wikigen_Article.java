





import java.util.List;
import java.util.ArrayList;

public class wikigen_Article extends HtmlProfile {

    private boolean generateTOC;
    private int nbColumns;



    public wikigen_Article(
        boolean generateTOC,        int nbColumns    ) {
        super(
        );
        this.generateTOC = generateTOC;
        this.nbColumns = nbColumns;
    }


    public boolean getGeneratetoc() {
        return generateTOC;
    }

    public void setGeneratetoc(boolean generateTOC) {
        this.generateTOC = generateTOC;
    }
    public int getNbcolumns() {
        return nbColumns;
    }

    public void setNbcolumns(int nbColumns) {
        this.nbColumns = nbColumns;
    }


}