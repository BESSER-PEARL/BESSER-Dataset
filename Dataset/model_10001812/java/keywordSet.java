





import java.util.List;
import java.util.ArrayList;

public class keywordSet  {

    private String keyword;





    private searchFacade searchfacade;




    private Product product;


    public keywordSet(
        String keyword    ) {
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public searchFacade getSearchfacade() {
        return searchfacade;
    }

    public void setSearchfacade(searchFacade searchfacade) {
        this.searchfacade = searchfacade;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}