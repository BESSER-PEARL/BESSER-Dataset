





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String property;
    private boolean inJail;
    private int INITIAL_POSITION;
    private int position;
    private int PASS_GO_MONEY;
    private None money;
    private None rand;
    private boolean isAI;
    private boolean isRetire;
    private String name;
    private None board;
    private boolean isBankrupt;
    private int INITIAL_MONEY;



    public Player(
        String property,        boolean inJail,        int INITIAL_POSITION,        int position,        int PASS_GO_MONEY,        None money,        None rand,        boolean isAI,        boolean isRetire,        String name,        None board,        boolean isBankrupt,        int INITIAL_MONEY    ) {
        this.property = property;
        this.inJail = inJail;
        this.INITIAL_POSITION = INITIAL_POSITION;
        this.position = position;
        this.PASS_GO_MONEY = PASS_GO_MONEY;
        this.money = money;
        this.rand = rand;
        this.isAI = isAI;
        this.isRetire = isRetire;
        this.name = name;
        this.board = board;
        this.isBankrupt = isBankrupt;
        this.INITIAL_MONEY = INITIAL_MONEY;
    }


    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public boolean getInjail() {
        return inJail;
    }

    public void setInjail(boolean inJail) {
        this.inJail = inJail;
    }
    public int getInitial_position() {
        return INITIAL_POSITION;
    }

    public void setInitial_position(int INITIAL_POSITION) {
        this.INITIAL_POSITION = INITIAL_POSITION;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
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
    public boolean getIsretire() {
        return isRetire;
    }

    public void setIsretire(boolean isRetire) {
        this.isRetire = isRetire;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public boolean getIsbankrupt() {
        return isBankrupt;
    }

    public void setIsbankrupt(boolean isBankrupt) {
        this.isBankrupt = isBankrupt;
    }
    public int getInitial_money() {
        return INITIAL_MONEY;
    }

    public void setInitial_money(int INITIAL_MONEY) {
        this.INITIAL_MONEY = INITIAL_MONEY;
    }


}