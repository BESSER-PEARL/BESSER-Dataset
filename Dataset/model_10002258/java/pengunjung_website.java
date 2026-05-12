





import java.util.List;
import java.util.ArrayList;

public class pengunjung_website  {






    private List<news_Interface> news_interfaces;




    private List<our_costumer_Interface> our_costumer_interfaces;


    public pengunjung_website(
    ) {
        this.news_interfaces = new ArrayList<>();
        this.our_costumer_interfaces = new ArrayList<>();
    }

    public pengunjung_website(
        ArrayList<news_Interface> news_interfaces,        ArrayList<our_costumer_Interface> our_costumer_interfaces    ) {
        this.news_interfaces = news_interfaces;
        this.our_costumer_interfaces = our_costumer_interfaces;
    }


    public List<news_Interface> getNews_interfaces() {
        return news_interfaces;
    }

    public void addNews_interface(News_interface news_interface) {
        this.news_interfaces.add(news_interface);
    }
    public List<our_costumer_Interface> getOur_costumer_interfaces() {
        return our_costumer_interfaces;
    }

    public void addOur_costumer_interface(Our_costumer_interface our_costumer_interface) {
        this.our_costumer_interfaces.add(our_costumer_interface);
    }

}