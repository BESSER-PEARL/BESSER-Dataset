





import java.util.List;
import java.util.ArrayList;

public class admin  {






    private List<news_Interface> news_interfaces;




    private List<our_costumer_Interface> our_costumer_interfaces;




    private List<our_costumer___major> our_costumer___majors;




    private List<news> newss;




    private List<produk> produks;


    public admin(
    ) {
        this.news_interfaces = new ArrayList<>();
        this.our_costumer_interfaces = new ArrayList<>();
        this.our_costumer___majors = new ArrayList<>();
        this.newss = new ArrayList<>();
        this.produks = new ArrayList<>();
    }

    public admin(
        ArrayList<news_Interface> news_interfaces,        ArrayList<our_costumer_Interface> our_costumer_interfaces,        ArrayList<our_costumer___major> our_costumer___majors,        ArrayList<news> newss,        ArrayList<produk> produks    ) {
        this.news_interfaces = news_interfaces;
        this.our_costumer_interfaces = our_costumer_interfaces;
        this.our_costumer___majors = our_costumer___majors;
        this.newss = newss;
        this.produks = produks;
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
    public List<our_costumer___major> getOur_costumer___majors() {
        return our_costumer___majors;
    }

    public void addOur_costumer___major(Our_costumer___major our_costumer___major) {
        this.our_costumer___majors.add(our_costumer___major);
    }
    public List<news> getNewss() {
        return newss;
    }

    public void addNews(News news) {
        this.newss.add(news);
    }
    public List<produk> getProduks() {
        return produks;
    }

    public void addProduk(Produk produk) {
        this.produks.add(produk);
    }

}