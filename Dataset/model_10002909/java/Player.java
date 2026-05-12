





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int position;
    private boolean isRetire;
    private boolean isAI;
    private boolean inJail;
    private int INITIAL_POSITION;
    private None rand;
    private int PASS_GO_MONEY;
    private String property;
    private boolean isBankrupt;
    private None board;
    private int INITIAL_MONEY;
    private String name;
    private None money;



    public Player(
        int position,        boolean isRetire,        boolean isAI,        boolean inJail,        int INITIAL_POSITION,        None rand,        int PASS_GO_MONEY,        String property,        boolean isBankrupt,        None board,        int INITIAL_MONEY,        String name,        None money    ) {
        this.position = position;
        this.isRetire = isRetire;
        this.isAI = isAI;
        this.inJail = inJail;
        this.INITIAL_POSITION = INITIAL_POSITION;
        this.rand = rand;
        this.PASS_GO_MONEY = PASS_GO_MONEY;
        this.property = property;
        this.isBankrupt = isBankrupt;
        this.board = board;
        this.INITIAL_MONEY = INITIAL_MONEY;
        this.name = name;
        this.money = money;
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
    public boolean getIsai() {
        return isAI;
    }

    public void setIsai(boolean isAI) {
        this.isAI = isAI;
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
    public None getRand() {
        return rand;
    }

    public void setRand(None rand) {
        this.rand = rand;
    }
    public int getPass_go_money() {
        return PASS_GO_MONEY;
    }

    public void setPass_go_money(int PASS_GO_MONEY) {
        this.PASS_GO_MONEY = PASS_GO_MONEY;
    }
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public boolean getIsbankrupt() {
        return isBankrupt;
    }

    public void setIsbankrupt(boolean isBankrupt) {
        this.isBankrupt = isBankrupt;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public int getInitial_money() {
        return INITIAL_MONEY;
    }

    public void setInitial_money(int INITIAL_MONEY) {
        this.INITIAL_MONEY = INITIAL_MONEY;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getMoney() {
        return money;
    }

    public void setMoney(None money) {
        this.money = money;
    }


}