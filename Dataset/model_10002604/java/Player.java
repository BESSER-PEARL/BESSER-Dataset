





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int PASS_GO_MONEY;
    private None money;
    private int INITIAL_MONEY;
    private int position;
    private boolean isRetire;
    private None board;
    private int INITIAL_POSITION;
    private None rand;
    private boolean isAI;
    private boolean isBankrupt;
    private None property;
    private boolean inJail;
    private String name;



    public Player(
        int PASS_GO_MONEY,        None money,        int INITIAL_MONEY,        int position,        boolean isRetire,        None board,        int INITIAL_POSITION,        None rand,        boolean isAI,        boolean isBankrupt,        None property,        boolean inJail,        String name    ) {
        this.PASS_GO_MONEY = PASS_GO_MONEY;
        this.money = money;
        this.INITIAL_MONEY = INITIAL_MONEY;
        this.position = position;
        this.isRetire = isRetire;
        this.board = board;
        this.INITIAL_POSITION = INITIAL_POSITION;
        this.rand = rand;
        this.isAI = isAI;
        this.isBankrupt = isBankrupt;
        this.property = property;
        this.inJail = inJail;
        this.name = name;
    }


    public int getPass_go_money() {
        return PASS_GO_MONEY;
    }

    public void setPass_go_money(int PASS_GO_MONEY) {
        this.PASS_GO_MONEY = PASS_GO_MONEY;
    }
    public None getMoney() {
        return money;
    }

    public void setMoney(None money) {
        this.money = money;
    }
    public int getInitial_money() {
        return INITIAL_MONEY;
    }

    public void setInitial_money(int INITIAL_MONEY) {
        this.INITIAL_MONEY = INITIAL_MONEY;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public boolean getIsretire() {
        return isRetire;
    }

    public void setIsretire(boolean isRetire) {
        this.isRetire = isRetire;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public int getInitial_position() {
        return INITIAL_POSITION;
    }

    public void setInitial_position(int INITIAL_POSITION) {
        this.INITIAL_POSITION = INITIAL_POSITION;
    }
    public None getRand() {
        return rand;
    }

    public void setRand(None rand) {
        this.rand = rand;
    }
    public boolean getIsai() {
        return isAI;
    }

    public void setIsai(boolean isAI) {
        this.isAI = isAI;
    }
    public boolean getIsbankrupt() {
        return isBankrupt;
    }

    public void setIsbankrupt(boolean isBankrupt) {
        this.isBankrupt = isBankrupt;
    }
    public None getProperty() {
        return property;
    }

    public void setProperty(None property) {
        this.property = property;
    }
    public boolean getInjail() {
        return inJail;
    }

    public void setInjail(boolean inJail) {
        this.inJail = inJail;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}