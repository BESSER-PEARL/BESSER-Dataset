





import java.util.List;
import java.util.ArrayList;

public class uma_Domain extends ContentCategory {






    private List<uma_Domain> uma_domains;


    public uma_Domain(
    ) {
        super(
        );
        this.uma_domains = new ArrayList<>();
    }

    public uma_Domain(
        ArrayList<uma_Domain> uma_domains    ) {
        this.uma_domains = uma_domains;
    }


    public List<uma_Domain> getUma_domains() {
        return uma_domains;
    }

    public void addUma_domain(Uma_domain uma_domain) {
        this.uma_domains.add(uma_domain);
    }

}