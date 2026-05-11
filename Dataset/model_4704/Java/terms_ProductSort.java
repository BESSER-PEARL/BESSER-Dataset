





import java.util.List;
import java.util.ArrayList;

public class terms_ProductSort extends Sort {






    private terms_Sort terms_sort;




    private List<terms_Sort> terms_sorts;


    public terms_ProductSort(
    ) {
        super(
        );
        this.terms_sorts = new ArrayList<>();
    }

    public terms_ProductSort(
        ArrayList<terms_Sort> terms_sorts    ) {
        this.terms_sorts = terms_sorts;
    }


    public terms_Sort getTerms_sort() {
        return terms_sort;
    }

    public void setTerms_sort(terms_Sort terms_sort) {
        this.terms_sort = terms_sort;
    }
    public List<terms_Sort> getTerms_sorts() {
        return terms_sorts;
    }

    public void addTerms_sort(Terms_sort terms_sort) {
        this.terms_sorts.add(terms_sort);
    }

}