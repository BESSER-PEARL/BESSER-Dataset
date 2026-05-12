





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String addres;
    private String name;
    private String card;



    public Client(
        String addres,        String name,        String card    ) {
        this.addres = addres;
        this.name = name;
        this.card = card;
    }


    public String getAddres() {
        return addres;
    }

    public void setAddres(String addres) {
        this.addres = addres;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCard() {
        return card;
    }

    public void setCard(String card) {
        this.card = card;
    }


}