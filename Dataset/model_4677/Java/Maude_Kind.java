





import java.util.List;
import java.util.ArrayList;

public class Maude_Kind extends Type {






    private List<Maude_Sort> maude_sorts;




    private Maude_Sort maude_sort;


    public Maude_Kind(
    ) {
        super(
        );
        this.maude_sorts = new ArrayList<>();
    }

    public Maude_Kind(
        ArrayList<Maude_Sort> maude_sorts    ) {
        this.maude_sorts = maude_sorts;
    }


    public List<Maude_Sort> getMaude_sorts() {
        return maude_sorts;
    }

    public void addMaude_sort(Maude_sort maude_sort) {
        this.maude_sorts.add(maude_sort);
    }
    public Maude_Sort getMaude_sort() {
        return maude_sort;
    }

    public void setMaude_sort(Maude_Sort maude_sort) {
        this.maude_sort = maude_sort;
    }

}