





import java.util.List;
import java.util.ArrayList;

public class StartGame  {

    private None p4;
    private int turn;
    private None p3;
    private None trick;
    private None t2;
    private None deck;
    private int bidNumber;
    private String playerOrder;
    private int lead;
    private None p1;
    private None p2;
    private None t1;





    private List<Trick> tricks;




    private List<Deck> decks;




    private List<Player> players;




    private List<Team> teams;


    public StartGame(
        None p4,        int turn,        None p3,        None trick,        None t2,        None deck,        int bidNumber,        String playerOrder,        int lead,        None p1,        None p2,        None t1    ) {
        this.p4 = p4;
        this.turn = turn;
        this.p3 = p3;
        this.trick = trick;
        this.t2 = t2;
        this.deck = deck;
        this.bidNumber = bidNumber;
        this.playerOrder = playerOrder;
        this.lead = lead;
        this.p1 = p1;
        this.p2 = p2;
        this.t1 = t1;
        this.tricks = new ArrayList<>();
        this.decks = new ArrayList<>();
        this.players = new ArrayList<>();
        this.teams = new ArrayList<>();
    }

    public StartGame(
        None p4,        int turn,        None p3,        None trick,        None t2,        None deck,        int bidNumber,        String playerOrder,        int lead,        None p1,        None p2,        None t1        ArrayList<Trick> tricks,        ArrayList<Deck> decks,        ArrayList<Player> players,        ArrayList<Team> teams    ) {
        this.p4 = p4;
        this.turn = turn;
        this.p3 = p3;
        this.trick = trick;
        this.t2 = t2;
        this.deck = deck;
        this.bidNumber = bidNumber;
        this.playerOrder = playerOrder;
        this.lead = lead;
        this.p1 = p1;
        this.p2 = p2;
        this.t1 = t1;
        this.tricks = tricks;
        this.decks = decks;
        this.players = players;
        this.teams = teams;
    }

    public None getP4() {
        return p4;
    }

    public void setP4(None p4) {
        this.p4 = p4;
    }
    public int getTurn() {
        return turn;
    }

    public void setTurn(int turn) {
        this.turn = turn;
    }
    public None getP3() {
        return p3;
    }

    public void setP3(None p3) {
        this.p3 = p3;
    }
    public None getTrick() {
        return trick;
    }

    public void setTrick(None trick) {
        this.trick = trick;
    }
    public None getT2() {
        return t2;
    }

    public void setT2(None t2) {
        this.t2 = t2;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getBidnumber() {
        return bidNumber;
    }

    public void setBidnumber(int bidNumber) {
        this.bidNumber = bidNumber;
    }
    public String getPlayerorder() {
        return playerOrder;
    }

    public void setPlayerorder(String playerOrder) {
        this.playerOrder = playerOrder;
    }
    public int getLead() {
        return lead;
    }

    public void setLead(int lead) {
        this.lead = lead;
    }
    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }
    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }
    public None getT1() {
        return t1;
    }

    public void setT1(None t1) {
        this.t1 = t1;
    }

    public List<Trick> getTricks() {
        return tricks;
    }

    public void addTrick(Trick trick) {
        this.tricks.add(trick);
    }
    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }
    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }
    public List<Team> getTeams() {
        return teams;
    }

    public void addTeam(Team team) {
        this.teams.add(team);
    }

}