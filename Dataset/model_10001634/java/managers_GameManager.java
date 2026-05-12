





import java.util.List;
import java.util.ArrayList;

public class managers_GameManager  {

    private int initialSmallID;
    private String playerHands;
    private String playerNames;
    private int playerTurn;
    private None minimumState;
    private String playerBets;
    private String playerIDs;
    private String stateOfPlayersArr;
    private String tableCards;
    private int initialBigID;
    private float raise;
    private int playersLeftInTheGame;
    private boolean newRound;
    private int dealer;
    private float smallblind;





    private List<common_Observer_Interface> common_observer_interfaces;




    private calculations_PokerRules calculations_pokerrules;


    public managers_GameManager(
        int initialSmallID,        String playerHands,        String playerNames,        int playerTurn,        None minimumState,        String playerBets,        String playerIDs,        String stateOfPlayersArr,        String tableCards,        int initialBigID,        float raise,        int playersLeftInTheGame,        boolean newRound,        int dealer,        float smallblind    ) {
        this.initialSmallID = initialSmallID;
        this.playerHands = playerHands;
        this.playerNames = playerNames;
        this.playerTurn = playerTurn;
        this.minimumState = minimumState;
        this.playerBets = playerBets;
        this.playerIDs = playerIDs;
        this.stateOfPlayersArr = stateOfPlayersArr;
        this.tableCards = tableCards;
        this.initialBigID = initialBigID;
        this.raise = raise;
        this.playersLeftInTheGame = playersLeftInTheGame;
        this.newRound = newRound;
        this.dealer = dealer;
        this.smallblind = smallblind;
        this.common_observer_interfaces = new ArrayList<>();
    }

    public managers_GameManager(
        int initialSmallID,        String playerHands,        String playerNames,        int playerTurn,        None minimumState,        String playerBets,        String playerIDs,        String stateOfPlayersArr,        String tableCards,        int initialBigID,        float raise,        int playersLeftInTheGame,        boolean newRound,        int dealer,        float smallblind        ArrayList<common_Observer_Interface> common_observer_interfaces    ) {
        this.initialSmallID = initialSmallID;
        this.playerHands = playerHands;
        this.playerNames = playerNames;
        this.playerTurn = playerTurn;
        this.minimumState = minimumState;
        this.playerBets = playerBets;
        this.playerIDs = playerIDs;
        this.stateOfPlayersArr = stateOfPlayersArr;
        this.tableCards = tableCards;
        this.initialBigID = initialBigID;
        this.raise = raise;
        this.playersLeftInTheGame = playersLeftInTheGame;
        this.newRound = newRound;
        this.dealer = dealer;
        this.smallblind = smallblind;
        this.common_observer_interfaces = common_observer_interfaces;
    }

    public int getInitialsmallid() {
        return initialSmallID;
    }

    public void setInitialsmallid(int initialSmallID) {
        this.initialSmallID = initialSmallID;
    }
    public String getPlayerhands() {
        return playerHands;
    }

    public void setPlayerhands(String playerHands) {
        this.playerHands = playerHands;
    }
    public String getPlayernames() {
        return playerNames;
    }

    public void setPlayernames(String playerNames) {
        this.playerNames = playerNames;
    }
    public int getPlayerturn() {
        return playerTurn;
    }

    public void setPlayerturn(int playerTurn) {
        this.playerTurn = playerTurn;
    }
    public None getMinimumstate() {
        return minimumState;
    }

    public void setMinimumstate(None minimumState) {
        this.minimumState = minimumState;
    }
    public String getPlayerbets() {
        return playerBets;
    }

    public void setPlayerbets(String playerBets) {
        this.playerBets = playerBets;
    }
    public String getPlayerids() {
        return playerIDs;
    }

    public void setPlayerids(String playerIDs) {
        this.playerIDs = playerIDs;
    }
    public String getStateofplayersarr() {
        return stateOfPlayersArr;
    }

    public void setStateofplayersarr(String stateOfPlayersArr) {
        this.stateOfPlayersArr = stateOfPlayersArr;
    }
    public String getTablecards() {
        return tableCards;
    }

    public void setTablecards(String tableCards) {
        this.tableCards = tableCards;
    }
    public int getInitialbigid() {
        return initialBigID;
    }

    public void setInitialbigid(int initialBigID) {
        this.initialBigID = initialBigID;
    }
    public float getRaise() {
        return raise;
    }

    public void setRaise(float raise) {
        this.raise = raise;
    }
    public int getPlayersleftinthegame() {
        return playersLeftInTheGame;
    }

    public void setPlayersleftinthegame(int playersLeftInTheGame) {
        this.playersLeftInTheGame = playersLeftInTheGame;
    }
    public boolean getNewround() {
        return newRound;
    }

    public void setNewround(boolean newRound) {
        this.newRound = newRound;
    }
    public int getDealer() {
        return dealer;
    }

    public void setDealer(int dealer) {
        this.dealer = dealer;
    }
    public float getSmallblind() {
        return smallblind;
    }

    public void setSmallblind(float smallblind) {
        this.smallblind = smallblind;
    }

    public List<common_Observer_Interface> getCommon_observer_interfaces() {
        return common_observer_interfaces;
    }

    public void addCommon_observer_interface(Common_observer_interface common_observer_interface) {
        this.common_observer_interfaces.add(common_observer_interface);
    }
    public calculations_PokerRules getCalculations_pokerrules() {
        return calculations_pokerrules;
    }

    public void setCalculations_pokerrules(calculations_PokerRules calculations_pokerrules) {
        this.calculations_pokerrules = calculations_pokerrules;
    }

}