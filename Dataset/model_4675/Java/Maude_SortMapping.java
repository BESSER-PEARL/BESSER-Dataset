





import java.util.List;
import java.util.ArrayList;

public class Maude_SortMapping extends RenMapping {

    private String to;





    private Maude_Sort maude_sort;


    public Maude_SortMapping(
        String to    ) {
        super(
        );
        this.to = to;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public Maude_Sort getMaude_sort() {
        return maude_sort;
    }

    public void setMaude_sort(Maude_Sort maude_sort) {
        this.maude_sort = maude_sort;
    }

}