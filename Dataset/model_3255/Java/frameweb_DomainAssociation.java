





import java.util.List;
import java.util.ArrayList;

public class frameweb_DomainAssociation extends Association {

    private String fetch;
    private String collection;
    private String order;
    private String cascade;



    public frameweb_DomainAssociation(
        String fetch,        String collection,        String order,        String cascade    ) {
        super(
        );
        this.fetch = fetch;
        this.collection = collection;
        this.order = order;
        this.cascade = cascade;
    }


    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }
    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getCascade() {
        return cascade;
    }

    public void setCascade(String cascade) {
        this.cascade = cascade;
    }


}