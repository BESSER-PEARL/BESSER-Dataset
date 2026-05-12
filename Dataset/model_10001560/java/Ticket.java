





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private int idCustomer;
    private String positionSeat;
    private int idTicket;
    private int statusSeat;
    private String timeExchange;
    private String positionSeatBelow;
    private int numberSeat;
    private String code;
    private int idCar;





    private Car car;




    private Customer customer;


    public Ticket(
        int idCustomer,        String positionSeat,        int idTicket,        int statusSeat,        String timeExchange,        String positionSeatBelow,        int numberSeat,        String code,        int idCar    ) {
        this.idCustomer = idCustomer;
        this.positionSeat = positionSeat;
        this.idTicket = idTicket;
        this.statusSeat = statusSeat;
        this.timeExchange = timeExchange;
        this.positionSeatBelow = positionSeatBelow;
        this.numberSeat = numberSeat;
        this.code = code;
        this.idCar = idCar;
    }


    public int getIdcustomer() {
        return idCustomer;
    }

    public void setIdcustomer(int idCustomer) {
        this.idCustomer = idCustomer;
    }
    public String getPositionseat() {
        return positionSeat;
    }

    public void setPositionseat(String positionSeat) {
        this.positionSeat = positionSeat;
    }
    public int getIdticket() {
        return idTicket;
    }

    public void setIdticket(int idTicket) {
        this.idTicket = idTicket;
    }
    public int getStatusseat() {
        return statusSeat;
    }

    public void setStatusseat(int statusSeat) {
        this.statusSeat = statusSeat;
    }
    public String getTimeexchange() {
        return timeExchange;
    }

    public void setTimeexchange(String timeExchange) {
        this.timeExchange = timeExchange;
    }
    public String getPositionseatbelow() {
        return positionSeatBelow;
    }

    public void setPositionseatbelow(String positionSeatBelow) {
        this.positionSeatBelow = positionSeatBelow;
    }
    public int getNumberseat() {
        return numberSeat;
    }

    public void setNumberseat(int numberSeat) {
        this.numberSeat = numberSeat;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public int getIdcar() {
        return idCar;
    }

    public void setIdcar(int idCar) {
        this.idCar = idCar;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}