# initial public offer
# bids: userid, num of shares, bidding price, timestamp
import collections


def main(bids, totalShare):
  origin = {}
  price_to_bids = collections.defaultdict(list)
  prices = []
  for bid in bids:
    origin[bid[0]] = bid[1]
    price_to_bids[bid[2]].append(bid)
    prices.append(bid[2])

  for price in price_to_bids:
    price_to_bids[price].sort(key=lambda x: x[3])

  prices = sorted(prices, reverse=True)
  for price in prices:
    if totalShare == 0:
      break
    cur_bids = price_to_bids[price]
    if len(cur_bids) == 1:
      cur_bid = cur_bids[0]
      allot = cur_bid[1] if cur_bid[1] < totalShare else totalShare
      cur_bid[1] -= allot
      totalShare -= allot
    else:
      while totalShare > 0 and any(bid[1] > 0 for bid in cur_bids):
        for bid in cur_bids:
          if totalShare == 0:
            break
          if bid[1] == 0:
            continue
          bid[1] -= 1
          totalShare -= 1

  print(bids)
  res = []
  for bid in bids:
    if bid[1] == origin[bid[0]]:
      res.append(bid[0])
  return sorted(res)


print(main([[1, 2, 5, 0], [2, 1, 4, 2], [3, 5, 4, 6]], 3))
