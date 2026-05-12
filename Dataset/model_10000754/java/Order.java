





import java.util.List;
import java.util.ArrayList;

public class Order  {






    private book book;




    private Payment_Interface payment_interface;




    private Client client;




    private Basket basket;


    public Order(
    ) {
    }



    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }
    public Payment_Interface getPayment_interface() {
        return payment_interface;
    }

    public void setPayment_interface(Payment_Interface payment_interface) {
        this.payment_interface = payment_interface;
    }
    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }
    public Basket getBasket() {
        return basket;
    }

    public void setBasket(Basket basket) {
        this.basket = basket;
    }

}